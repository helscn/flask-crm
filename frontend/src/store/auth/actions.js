import axios from "axios";

export function refreshLogin({ commit }) {
  return new Promise((resolve, reject) => {
    axios({
      method: "get",
      url: "/auth/gettoken"
    })
      .then(res => {
        commit("changeLogin", res.data);
        resolve(res);
      })
      .catch(err => {
        commit("logout");
        reject(err);
      });
  });
}

export function login({ commit }, { username, password }) {
  return new Promise((resolve, reject) => {
    axios({
      method: "post",
      url: "/auth/login",
      data: {
        username: username,
        password: password
      }
    })
      .then(res => {
        commit("changeLogin", res.data);
        resolve(res);
      })
      .catch(err => {
        commit("logout");
        reject(err);
      });
  });
}

export function logout({ commit }) {
  commit("logout");
}
