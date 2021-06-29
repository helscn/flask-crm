import Vue from "vue";
import axios from "axios";
import VueCookies from "vue-cookies";

Vue.use(VueCookies);
Vue.$cookies.config("7d");

axios.defaults.timeout = 5000;
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded;charset=UTF-8";
axios.defaults.baseURL = "http://localhost:5000";

axios.interceptors.request.use(
  //请求拦截器
  config => {
    if (Vue.$cookies.isKey("Token")) {
      config.headers.Token = Vue.$cookies.get("Token");
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// axios.interceptors.response.use(
//   //响应拦截器
//   data => {
//     return data;
//   },
//   error => {
//     if (error.status == 401) {
//       alert("未认证用户，请重新登录！");
//     }
//     return Promise.reject(error);
//   }
// );

Vue.prototype.$axios = axios;
