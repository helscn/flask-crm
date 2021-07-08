import Vue from "vue";

export function isLogined(state) {
  return !!(state.id && Vue.$cookies.isKey("Token"));
}
