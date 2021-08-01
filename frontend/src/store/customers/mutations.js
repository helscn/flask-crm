export function setCustomers(state, newState) {
  state.data = newState.data;
}

export function setCustomersFilter(state, filter) {
  state.validFilter = filter;
}

export function clearCustomers(state) {
  state.data = [];
}

export function setContacts(state, newState) {
  state.contacts = newState.data;
}

export function clearContacts(state) {
  state.contacts = [];
}

export function setLoading(state) {
  state.loading = true;
}

export function setLoaded(state) {
  state.loading = false;
}
