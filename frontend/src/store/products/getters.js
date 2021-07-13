export function validProducts(state) {
  return state.data.filter(product => product.valid);
}

export function productsCount(state) {
  return state.data.length;
}

export function productCategories(state) {
  return state.categories.map(category => category.name);
}

export function categoriesCount(state) {
  return state.categories.length;
}
