export function validProducts(state) {
  return state.data.filter(product => product.valid);
}

export function total(state) {
  return state.data.length;
}
