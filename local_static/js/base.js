document.addEventListener('DOMContentLoaded', () => {
  
  const navbar = document.querySelector('.navbar');
  const navbar_free_quote = document.querySelector('.navbar-free-quote');

  window.addEventListener('scroll', () => {

    // Shrink Navbar on Page Scroll
    //
    // Change the appearance of the navbar when the user scrolls down the page
    if (window.scrollY > 1) {

      // "Minimize" the navbar
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');

      // "Minimize" the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-true');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-false');
    } else {

      // "Maximize" the navbar
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');

      // "Maximize" the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-false');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-true');
    }
  })

  // Underline Active Navbar Links & Toggle Free Quote Button Visibility
  //
  // Assign the .active class to the current page's nav-link which decorates it
  // with an underscore (to give an indication which page is the current page)
  // & display the 'Free Quote' button -not- on contact.html or thanks.html.
  if (document.querySelector('.container-fluid').classList.contains('index-page')) {
    document.querySelector('.nav-link-home').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('services-page')) {
    document.querySelector('.nav-link-services').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('ourwork-page')) {
    document.querySelector('.nav-link-ourwork').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('about-page')) {
    document.querySelector('.nav-link-about').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('contact-page')) {
    document.querySelector('.nav-link-contact').classList.add('active');
  }
})