<template>
  <input type="text" class="input" :value="value" v-on="listeners" />
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: "Hello, Vue.js!",
    },
  },
  computed: {
    listeners() {
      return {
        ...this.$listeners,
        input: (event) => this.$emit("input", event.target.value),
      };
    },
  },
};
</script>

<style scoped>
.input {
  width: 100%;
  padding: 8px 10px;
  border: 1px solid #b1b1b1;
  line-height: 25px;
}
.input:focus {
    border: 2px solid rgb(66, 158, 233);
}
</style>
