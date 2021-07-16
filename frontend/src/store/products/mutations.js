export function setProducts(state, newState) {
  state.data = newState.data;
}

export function clearProducts(state) {
  state.data = [];
}

export function setSuppliers(state, newState) {
  state.suppliers = newState.data;
}

export function clearSuppliers(state) {
  state.suppliers = [];
}

export function setCategories(state, newState) {
  state.categories = newState.data;
}

export function clearCategories(state) {
  state.categories = [];
}

export function setLoading(state) {
  state.loading = true;
}

export function setLoaded(state) {
  state.loading = false;
}
