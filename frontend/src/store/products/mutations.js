export function setProducts(state, newState) {
  state.data = newState.data;
}

export function clearProducts(state) {
  state.data = [];
}
