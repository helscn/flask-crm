import Vue from "vue";

export function changeLogin(state, user) {
  state.id = user.id;
  state.username = user.username;
  state.nickname = user.nickname;
  state.role_id = user.role_id;
  state.role_name = user.role_name;
  Vue.$cookies.set("Token", user.token);
}

export function logout(state) {
  state.id = "";
  state.username = "";
  state.nickname = "";
  state.role_id = "";
  state.role_name = "";
  Vue.$cookies.remove("Token");
}
