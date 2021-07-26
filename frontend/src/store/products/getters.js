export function filteredProducts(state) {
  if (state.validFilter == "valid") {
    return state.data.filter(product => product.valid == 1);
  } else if (state.validFilter == "unvalid") {
    return state.data.filter(product => product.valid == 0);
  } else {
    return state.data;
  }
}

export function productsCount(state) {
  return state.data.length;
}

export function productSuppliers(state) {
  return state.suppliers.map(supplier => supplier.name);
}

export function suppliersCount(state) {
  return state.suppliers.length;
}

export function productCategories(state) {
  return state.categories.map(category => category.name);
}

export function categoriesCount(state) {
  return state.categories.length;
}

export function cartItemsCount(state) {
  return state.cart.length;
}
