// Test the real browser script at its wallet/DOM boundary, without payments.
const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const ADDRESS = 'sat@lightning-goats.com';

function setup(provider, clipboard) {
  const filename = path.join(__dirname, '../assets/donations.js');
  assert.ok(fs.existsSync(filename), 'Donation script is not implemented');
  function element() {
    return {hidden: true, textContent: '', events: {}, attributes: {},
      addEventListener(type, fn) { this.events[type] = fn; },
      setAttribute(key, value) { this.attributes[key] = value; },
      removeAttribute(key) { delete this.attributes[key]; }};
  }
  const links = [element(), element(), element()];
  const section = element();
  section.dataset = {lightningAddress: ADDRESS};
  section.querySelectorAll = () => links;
  const status = element();
  const copy = element();
  const document = {getElementById(id) {
    return {support: section, 'donation-status': status, 'copy-lightning-address': copy}[id] || null;
  }};
  const window = {webln: provider};
  vm.runInNewContext(fs.readFileSync(filename, 'utf8'), {window, document, navigator: {clipboard}});
  function event(overrides = {}) {
    return {button: 0, ctrlKey: false, metaKey: false, shiftKey: false, altKey: false,
      prevented: false, stopped: false,
      preventDefault() {this.prevented = true;}, stopPropagation() {this.stopped = true;}, ...overrides};
  }
  return {links, section, status, copy, window, event};
}

test('never opens a wallet or requests payment on page load', () => {
  let called = 0;
  setup({enable() {called++;}, lnurl() {called++;}});
  assert.equal(called, 0);
});

test('QR, address and primary button all send the same recipient to WebLN', async () => {
  const calls = [];
  const state = setup({async enable() {calls.push('enable');}, async lnurl(address) {
    calls.push(address); return {status: 'OK', data: {preimage: '1'.repeat(64), paymentHash: '2'.repeat(64)}};
  }});
  for (const link of state.links) {
    const event = state.event();
    await link.events.click(event);
    assert.equal(event.prevented, true);
    assert.equal(event.stopped, true);
  }
  assert.deepEqual(calls, ['enable', ADDRESS, 'enable', ADDRESS, 'enable', ADDRESS]);
  assert.match(state.status.textContent, /Thank you/);
  assert.equal(state.section.attributes['aria-busy'], undefined);
});

test('without WebLN or optional lnurl support, the native href is not prevented', async () => {
  for (const provider of [undefined, {}, {enable() {}}, {lnurl() {}}]) {
    const state = setup(provider);
    const event = state.event();
    await state.links[0].events.click(event);
    assert.equal(event.prevented, false);
  }
});

test('a late-injected extension is detected at click time', async () => {
  const state = setup(undefined);
  let called;
  state.window.webln = {async enable() {}, async lnurl(address) {called = address;}};
  await state.links[0].events.click(state.event());
  assert.equal(called, ADDRESS);
});

test('denied wallet permission never proceeds to payment', async () => {
  let paid = 0;
  const state = setup({async enable() {throw new Error('User rejected');}, async lnurl() {paid++;}});
  await state.links[0].events.click(state.event());
  assert.equal(paid, 0);
  assert.match(state.status.textContent, /Check your wallet before retrying/);
  assert.doesNotMatch(state.status.textContent, /Thank you/);
});

test('failed and empty wallet results never claim a completed donation', async () => {
  for (const response of [{status: 'ERROR', reason: '<script>secret</script>'}, {}, {status: 'OK'}, null]) {
    const state = setup({async enable() {}, async lnurl() {return response;}});
    await state.links[0].events.click(state.event());
    assert.doesNotMatch(state.status.textContent, /Thank you|secret|<script>/);
    assert.match(state.status.textContent, /wallet/);
  }
});

test('double click does not start a duplicate payment', async () => {
  let release;
  let called = 0;
  const gate = new Promise(resolve => {release = resolve;});
  const state = setup({async enable() {}, async lnurl() {called++; await gate; return {status:'ERROR'};}});
  const first = state.links[0].events.click(state.event());
  await Promise.resolve();
  const secondEvent = state.event();
  await state.links[1].events.click(secondEvent);
  assert.equal(called, 1);
  assert.equal(secondEvent.prevented, true);
  release();
  await first;
});

test('modified and middle clicks retain their ordinary behavior', async () => {
  const state = setup({enable() {throw Error('must not call');}, lnurl() {throw Error('must not call');}});
  for (const overrides of [{ctrlKey:true},{metaKey:true},{shiftKey:true},{altKey:true},{button:1}]) {
    const event = state.event(overrides);
    await state.links[0].events.click(event);
    assert.equal(event.prevented, false);
  }
});

test('copy uses only the public Lightning address and handles permission errors', async () => {
  let copied;
  const ok = setup(undefined, {async writeText(value) {copied = value;}});
  assert.equal(ok.copy.hidden, false);
  await ok.copy.events.click();
  assert.equal(copied, ADDRESS);
  assert.match(ok.status.textContent, /copied/);
  for (const clipboard of [undefined, {async writeText() {throw Error('blocked');}}]) {
    const state = setup(undefined, clipboard);
    await state.copy.events.click();
    assert.match(state.status.textContent, /Select and copy/);
  }
});
