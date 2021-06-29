export function refreshLogin({ commit }, that) {
  that
    .$axios({
      method: "get",
      url: "/auth/gettoken"
    })
    .then(res => {
      commit("changeLogin", res.data);
      that.$cookies.set("Token", res.data.token);
    })
    .catch(error => {
      that.$router.push("/login");
    });
}
