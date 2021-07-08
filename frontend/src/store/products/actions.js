import Vue from "vue";
import axios from "axios";

export function fetchProducts({ commit }) {
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/api/products"
    })
      .then(res => {
        commit("setProducts", res.data);
        resolve(res);
      })
      .catch(err => {
        commit("clearProducts");
        reject(err);
      });
  });
}
