export function refreshLogin ({commit},that) {
    that.$axios({
        method: "get",
        url: "/auth/gettoken"
    }).then(res=>{
        commit('changeLogin',res.data)
    }).catch(error=>{
        that.$router.push("/login");
    })
}
