import MainLayout from "layouts/MainLayout";

const routes = [
  {
    path: "/",
    component: MainLayout,
    children: [
      {
        path: "",
        component: () => import("pages/Index.vue")
      },
      {
        path: "projects",
        component: () => import("pages/ProjectsView.vue")
      },
      {
        path: "products",
        component: () => import("layouts/ProductsLayout.vue"),
        children: [
          {
            path: "all",
            component: () => import("pages/products/AllProducts.vue")
          }
        ]
      },
      {
        path: "upload",
        component: () => import("pages/Upload.vue")
      }
    ]
  },
  {
    path: "/login",
    component: () => import("pages/Login.vue")
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "*",
    component: () => import("pages/Error404.vue")
  }
];

export default routes;
