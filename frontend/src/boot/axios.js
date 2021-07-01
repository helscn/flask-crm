import Vue from "vue";
import axios from "axios";
import VueCookies from "vue-cookies";

// 载入 Vue-Cookies 插件
Vue.use(VueCookies);
Vue.$cookies.config("1h");

// 配置 Axios 默认请求参数：
// 开发环境请求API接口地址
axios.defaults.baseURL = "http://localhost:5000";

// 设置API跨域访问，同时需要在后端服务器做跨域配置
axios.defaults.withCredentials = true;
axios.defaults.crossDomain = true;

// 默认请求超时时间，单位ms
axios.defaults.timeout = 5000;

// 设置请求 Content-Type 类型
axios.defaults.headers.get["Content-Type"] =
  "application/x-www-form-urlencoded;charset=UTF-8";
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded;charset=UTF-8";

// 设置请求前置拦截器;
// axios.interceptors.request.use(
//   config => {
//     if (Vue.$cookies.isKey("Token")) {
//       config.headers.Token = Vue.$cookies.get("Token");
//     }
//     return config;
//   },
//   error => {
//     return Promise.reject(error);
//   }
// );

// 设置请求响应拦截器
axios.interceptors.response.use(
  data => {
    return data;
  },
  error => {
    if (error.response.status == 401) {
      Vue.$cookies.remove("Token");
    }
    return Promise.reject(error);
  }
);

Vue.prototype.$axios = axios;
