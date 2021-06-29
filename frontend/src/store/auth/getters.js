export function isLogined (state) {
    return !!(state.id && state.token)
}
