import Vue from "vue";
import axios from "axios";

axios.defaults.timeout = 3000;
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded;charset=UTF-8";
axios.defaults.baseURL = "http://localhost:5000";

axios.interceptors.request.use(
  config => {
    if (localStorage.getItem("Token")) {
      config.headers.Token = localStorage.getItem("Token");
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

Vue.prototype.$axios = axios;
