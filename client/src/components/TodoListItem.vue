<template>
  <li class="content">
    {{ todo.text }}
    <button class="remove-btn" @click="$emit('remove', todo.id)">×</button>
  </li>
</template>
<script>
export default {
  props: {
    todo: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.remove-btn {
  background: transparent;
  color: #e7063f;
  border-color: #e7063f;
  text-align: center;
  vertical-align: middle;
  border: 1px solid transparent;
  line-height: 1.5;
  border-radius: 0.25rem;
  cursor: pointer;
}

.remove-btn:hover {
  background: #e7063f;
  color: white;
}
.content{
    border-bottom: 1px solid rgb(223, 223, 223);
    padding: 8px 0px;
    line-height: 25px;
    font-size: 18px;
}
.content:hover{
  background: rgb(236, 236, 236);
}
</style>