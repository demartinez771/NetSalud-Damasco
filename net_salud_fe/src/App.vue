<script>
import MiComponente from "./components/patientRecord.vue";

export default {
  name: "app",
  components: {
    MiComponente,
},
};
</script>

<template>
  <div id="app" class="app">
    <div class="header">
      <img src="./assets/Logo.png" alt="">  
      <h1>NetSalud</h1>
      <h2>La salud a tus manos</h2>
        <nav>
            <button v-if="is_auth" v-on:click="loadHome" > Inicio </button>
            <button v-if="is_auth" v-on:click="loadPatientRecord"> RegistroPaciente </button>
            <button v-if="is_auth" v-on:click="loaddoctorRecord"> RegistroMedico </button>
            <button v-if="is_auth" v-on:click="loadFamilyRecord"> RegistroFamiliar </button>
            <button v-if="is_auth" v-on:click="loadPatientConsult"> ConsultarPaciente </button>
            <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
        </nav>
    </div>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
