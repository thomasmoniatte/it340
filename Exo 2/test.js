const getBalance = require('./bank');
const DAO = require('./bankDAO');
afterEach(() => {
  // restore the spy created with spyOn
  jest.restoreAllMocks();
});

test('getBalance', () => {
  const spy = jest.spyOn(getBalance, 'retrievingBalance').mockImplementation(()=>{console.log('in mock')});
  const retrievedBalance = getBalance.retrievingBalance();

  expect(spy).toHaveBeenCalled();
  expect(retrievedBalance).toBe(true);
});

