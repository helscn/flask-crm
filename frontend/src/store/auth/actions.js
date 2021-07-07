import Vue from "vue";
import axios from "axios";

export function refreshLogin({ commit }) {
  return axios({
    method: "get",
    url: "/auth/gettoken"
  })
    .then(res => {
      commit("changeLogin", res.data);
    })
    .catch(err => {
      commit("logout");
    });
}

export function login({ commit }, { username, password }) {
  return axios({
    method: "post",
    url: "/auth/login",
    data: {
      username: username,
      password: password
    }
  }).then(res => {
    commit("changeLogin", res.data);
  });
}

export function logout({ commit }) {
  commit("logout");
}
