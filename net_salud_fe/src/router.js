import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import patientRecord from "./components/patientRecord";
import home from "./components/home";
import doctorRecord from "./components/doctorRecord";
import familyRecord from "./components/familyRecord";
import patientConsult from "./components/patientConsult";
import logIn from "./components/logIn";
import user from "./components/user";
const routes = [
  {
    path: "/auxiliar/inicio",
    name: "home",
    component: home,
  },
  {
    path: "/auxiliar/registrar-paciente",
    name: "patientRecord",
    component: patientRecord,
  },
  {
    path: "/auxiliar/registrar-medico",
    name: "doctorRecord",
    component: doctorRecord,
  },
  {
    path: "/auxiliar/registrar-familiar",
    name: "familyRecord",
    component: familyRecord,
  },
  {
    path: "/auxiliar/consultar-paciente",
    name: "patientConsult",
    component: patientConsult,
  },
  {
    path: "/auxiliar/logIn",
    name: "logIn",
    component: logIn,
  },
  {
    path: "/auxiliar/usuario/",
    name: "user",
    component: user,
  },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
