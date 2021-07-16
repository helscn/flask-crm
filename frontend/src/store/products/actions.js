import Vue from "vue";
import axios from "axios";

export function fetchProducts({ commit }) {
  commit("setLoading");
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/api/products"
    })
      .then(res => {
        commit("setProducts", res.data);
        commit("setLoaded");
        resolve(res);
      })
      .catch(err => {
        commit("clearProducts");
        commit("setLoaded");
        reject(err);
      });
  });
}

export function fetchSuppliers({ commit }) {
  commit("setLoading");
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/api/products/suppliers"
    })
      .then(res => {
        commit("setSuppliers", res.data);
        commit("setLoaded");
        resolve(res);
      })
      .catch(err => {
        commit("clearSuppliers");
        commit("setLoaded");
        reject(err);
      });
  });
}

export function fetchCategories({ commit }) {
  commit("setLoading");
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/api/products/categories"
    })
      .then(res => {
        commit("setCategories", res.data);
        commit("setLoaded");
        resolve(res);
      })
      .catch(err => {
        commit("clearCategories");
        commit("setLoaded");
        reject(err);
      });
  });
}
