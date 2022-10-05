<script>
import axios from 'axios';

export default {
  data: function () {
    return {
      familiar: {
        documento: "",
        parentesco: "",
        correo: "",
        username: "",
        familiar_documento: "",
      }
    }
  },

  methods: {
    registroFamiliar: function () {
      axios.post(
        "https://netsalud-be.herokuapp.com/familiar/",
        this.familiar,
        { headers: {} }
      )

        .then((result) => {
          alert("Familiar Registrado exitosamente!")
          this.$emit('registroFamiliar')
        })
        .catch((error) => {
          console.log(error);
          alert("Upps No se ha podido registrar el familiar :(")
        })
    }
  }
}

</script>
  
<template>
  <div id="rp" class="registro-familiar">
    <main>
      <form v-on:submit.prevent="registroFamiliar">
        <div>
          <label>Documento:</label>
          <input type="text" v-model="familiar.documento" id="documento" required>
        </div>

        <div>
          <label>Parentesco:</label>
          <input type="text" v-model="familiar.parentesco" id="parentesco" required>
        </div>

        <div>
          <label>Correo:</label>
          <input type="text" v-model="familiar.correo" id="correo" required>
        </div>

        <div>
          <label>Username:</label>
          <input type="text" v-model="familiar.username" id="username" required>
        </div>

        <div>
          <label>Documento del Familiar:</label>
          <input type="text" v-model="familiar.familiar_documento" id="familiar_documento" required>
        </div>

        <button type="submit">Registrar</button>

      </form>
    </main>


  </div>
</template>
  
<style>
form label {
  font-size: 17px;
  display: inline-flexbox;
  width: 130px;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;
  border-radius: 10px;
  color: #0d0e0d;
}

.registro-familiar {
  margin-top: 50px;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 400px;
  height: 600px;
  margin: 0 0 0 40px;
  flex-direction: column;
  padding: 10px;
  display: flex;
  background: #e3f2fd;
  border-radius: 20px;
  justify-content: space-evenly;
  align-items: center;
  border: 5px solid #2e2d4d;
}


form input {
  width: 300px;
  height: 40px;
  display: block;
  background: #fafafa;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;
  border-radius: 10px;
  color: #050505;
}

button {
  width: 300px;
  height: 50px;
  background: #2e2d4d;
  border-radius: 10px;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;

  color: #fafafa;
}
</style>