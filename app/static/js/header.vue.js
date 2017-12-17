var navbar = new Vue({
  el: '#navbar',
  data: {
    hamburger_active: false
  },
  // bind event handlers to the `handleResize` method
  mounted: function () {
    window.addEventListener('resize', this.untoggleHamburger);
  },
  beforeDestroy: function () {
    window.removeEventListener('resize', this.untoggleHamburger);
  },
  methods: {
    toggleMenu: function () {
      this.hamburger_active = !this.hamburger_active;
    },
    untoggleHamburger: function () {
        this.hamburger_active = false;
    }
  }
});

