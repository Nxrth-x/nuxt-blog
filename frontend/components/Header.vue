<template>
  <header class="container">
    <div class="circle">
      <p>N</p>
    </div>
    <div class="links">
      <a href="#">Blog</a>
      <a href="#">About</a>
    </div>
  </header>
</template>

<script>
</script>

<style lang="scss" scoped>
@import "../scss/variables.scss";

header {
  padding: 1rem 0;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

div.circle {
  width: 3rem;
  height: 3rem;

  display: grid;
  place-items: center;

  color: $white;

  background: linear-gradient(45deg, $pink, $red, $orange);

  border-radius: 50%;
}

div.links {
  display: flex;
  gap: 1rem;

  a {
    text-transform: uppercase;
    letter-spacing: 2px;

    color: $gray;

    border-bottom: 2px solid transparent;

    transition: $transition;

    &:hover {
      color: $pink;
      border-bottom: 2px solid $pink;
    }
  }
}
</style>