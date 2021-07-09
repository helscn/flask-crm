import MainLayout from "layouts/MainLayout";

const routes = [
  {
    path: "/",
    meta: { title: "首页", icon: "home" },
    component: MainLayout,
    children: [
      {
        path: "",
        component: () => import("pages/Index.vue")
      },
      {
        path: "projects",
        meta: { title: "我的项目", icon: "widgets" },
        component: () => import("pages/ProjectsView.vue")
      },
      {
        path: "products",
        meta: { title: "我的产品", icon: "business_center" },
        component: () => import("layouts/ProductsLayout.vue"),
        children: [
          {
            path: "",
            component: () => import("pages/products/ShowProducts.vue")
          },

          {
            path: "new",
            meta: { title: "新建产品", icon: "add_circle" },
            component: () => import("pages/products/NewProduct.vue")
          },

          {
            path: "all",
            meta: { title: "所有产品", icon: "business_center" },
            component: () => import("pages/products/AllProducts.vue")
          }
        ]
      },
      {
        path: "upload",
        meta: { title: "上传文件" },
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
