import Vue from "vue";
import axios from "axios";
import VueCookies from "vue-cookies";

Vue.use(VueCookies);
Vue.$cookies.config("7d");

axios.defaults.timeout = 3000;
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded;charset=UTF-8";
axios.defaults.baseURL = "http://localhost:5000";

axios.interceptors.request.use(
  //请求拦截器
  config => {
    // if (localStorage.getItem("Token")) {
    //   config.headers.Token = localStorage.getItem("Token");
    // }
    if (Vue.$cookies.isKey("Token")) {
      config.headers.Token = Vue.$cookies.get("Token");
    }
    return config;
  },
  error => {
    console.log(error.response.status);
    console.log(error.response.data);
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  //响应拦截器
  data => {
    return data;
  },
  error => {
    console.log(error.response.status);
    console.log(error.response.data);
    console.log(Vue.$router);
    if (error.status == 401) {
      Vue.$router.push("/login");
    } else {
      return Promise.reject(error);
    }
  }
);

Vue.prototype.$axios = axios;
