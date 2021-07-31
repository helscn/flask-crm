import axios from "axios";

export function fetchCustomers({ commit }) {
  commit("setLoading");
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/api/customers"
    })
      .then(res => {
        commit("setCustomers", res.data);
        commit("setLoaded");
        resolve(res);
      })
      .catch(err => {
        commit("clearCustomers");
        commit("setLoaded");
        reject(err);
      });
  });
}

export function fetchContacts({ commit }) {
  commit("setLoading");
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/api/customers/contacts"
    })
      .then(res => {
        commit("setContacts", res.data);
        commit("setLoaded");
        resolve(res);
      })
      .catch(err => {
        commit("clearContacts");
        commit("setLoaded");
        reject(err);
      });
  });
}
