export function validCustomers(state) {
  return state.data.filter(customer => customer.valid != 0);
}

export function validContacts(state) {
  return state.contacts.filter(contacter => contacter.valid != 0);
}
