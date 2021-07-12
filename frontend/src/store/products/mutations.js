export function setProducts(state, newState) {
  state.data = newState.data;
}

export function clearProducts(state) {
  state.data = [];
}

export function setLoading(state) {
  state.loading = true;
}

export function setLoaded(state) {
  state.loading = false;
}
