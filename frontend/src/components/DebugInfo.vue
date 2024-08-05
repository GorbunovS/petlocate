<template>
  <div class="debug-info">
    <p>Selected ID: {{ selectedItemId }}</p>
  </div>
</template>

<script>
export default {
  name: 'DebugInfo',
  props: {
    selectedItemId: {
      type: Number,
      required: true
    }
  }
};
</script>

<style scoped>
.debug-info {
  position: absolute;
  bottom: 10px;
  left: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 5px;
  z-index: 1000;
}
</style>
