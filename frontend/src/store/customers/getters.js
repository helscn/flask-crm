export function filteredCustomers(state) {
  if (state.validFilter == "valid") {
    return state.data.filter(customer => customer.valid != 0);
  } else if (state.validFilter == "unvalid") {
    return state.data.filter(customer => customer.valid == 0);
  } else {
    return state.data;
  }
}
