<script>
import MyComponent2 from "./MyComponent2.vue";
export default {
  name: "MiComponente",
  components: { MyComponent2 },
  data() {
    return {
      subtitulo: "soy el subtitulo de mi componente",
      titles: ["david es la verga", "david juega mal lol"],
    };
  },
};
</script>

<template>
  <div>
    <h1>Este es Mi componente</h1>
    <h2>{{ subtitulo }}</h2>
    <li v-for="title in titles" :key="title">
      <MyComponent2 :title="title" />
    </li>
  </div>
</template>
