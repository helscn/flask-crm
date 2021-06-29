export function changeLogin(state, user) {
  state.id = user.id;
  state.username = user.username;
}

export function logout(state) {
  state.id = "";
  state.username = "";
  state.token = "";
  localStorage.removeItem("Token");
}
