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
