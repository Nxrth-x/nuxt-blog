<template>
  <div class="profile">
    <div class="profile-image">
      <img
        src="https://avatars.githubusercontent.com/u/64004309?v=4"
        alt="Eder Lima"
      />
    </div>
    <div class="profile-info">
      <p class="poster">Eder Lima</p>
      <p class="date">March 5, 2021.</p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import "../scss/variables.scss";

div.profile {
  display: flex;
  align-items: center;
  gap: 1rem;

  div.profile-image {
    width: 4rem;
    height: 4rem;

    display: grid;
    place-items: center;

    border: 2px solid $red;
    border-radius: 50%;

    img {
      width: 90%;

      border-radius: 50%;
    }
  }

  div.profile-info {
    p.poster {
      background: linear-gradient(90deg, $pink, $red, $orange);
      -webkit-text-fill-color: transparent;
      background-clip: text;

      font-weight: 700;
      letter-spacing: 2px;
    }

    p.date {
      color: $gray;
      font-size: 0.9rem;
      letter-spacing: 1px;
    }
  }
}
</style>