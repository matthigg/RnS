document.addEventListener('DOMContentLoaded', () => {
  
  const navbar = document.querySelector('.navbar');
  const navbar_brand = document.querySelector('.navbar-brand');
  const navbar_free_quote = document.querySelector('.navbar-free-quote');

  window.addEventListener('scroll', () => {

    // Shrink Navbar on Page Scroll
    //
    // Change the appearance of the navbar when the user scrolls down the page
    if (window.scrollY > 1) {

      // Shrink the navbar
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');

      // Shrink the navbar brand/logo
      navbar_brand.classList.add('shrink');
      navbar_brand.classList.remove('expand');

      // Reposition/move up the 'free quote' button
      navbar_free_quote.classList.add('navbar-free-quote-minimized-true');
      navbar_free_quote.classList.remove('navbar-free-quote-minimized-false');
    } else {

      // Expand the navbar
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');

      // Shrink the navbar brand/logo
      navbar_brand.classList.add('expand');
      navbar_brand.classList.remove('shrink');

      // Reposition/move down the 'free quote' button
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
  } else if (document.querySelector('.container-fluid').classList.contains('our-work-page')) {
    document.querySelector('.nav-link-our-work').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('about-page')) {
    document.querySelector('.nav-link-about').classList.add('active');
    document.querySelector('.navbar-free-quote').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('contact-page')) {
    document.querySelector('.nav-link-contact').classList.add('active');
  }

  // Contact Form 
  //
  // Add an asterisk * next to each contact form field that is a required field
  if (document.querySelector('.contact-form') !== null) {
    const labels = document.querySelectorAll('label')
    labels.forEach((label) => {
      if (
        label.innerHTML === 'Name' ||
        label.innerHTML === 'Email' ||
        label.innerHTML === 'Message'
      ) {
        label.innerHTML += ' <span class="required-field-asterisk">*</span>';
      }
    })
  }

  // Modals
  //
  // When a <div> .section-1-baap-group element or any of its children (all of 
  // which are located in ourwork.html and together represent a 'before & after'
  // picture group) are clicked, search/scrounge for the appropriate data-id
  // attribute's value, which identifies that particular 'before & after' picture
  // group. This data-id value is then used to construct the before & after <img>
  // src attributes in the re-usable Bootstrap modal HTML markup located in 
  // ourwork-modals.html. 
  //
  // Additionally, this JavaScript will scrounge for the relative static img path 
  // (ie. /static/img/...) which is stored as data-src in the same HTML element 
  // as the data-id, and the data-src attribute's value, together with the data-id 
  // attribute's value is then used to construct a path to the before & after 
  // images that we're looking for.
  const baap_groups = document.querySelectorAll('.section-1-baap-group');
  baap_groups.forEach((baap_group) => {
    baap_group.addEventListener('click', (event) => {
      let element = event.target;
      if (element.dataset.id === undefined) {
        while (element.parentNode) {
          element = element.parentNode;
          if (element.dataset.id) {
            assignModalImage(element.dataset.src, element.dataset.id);
            return
          } 
        }
      } else {
        assignModalImage(element.dataset.src, element.dataset.id);
      }
    })
  })

  function assignModalImage(src, id) {
    const img_src_before = src + '/' + id + '-before.jpg';
    const img_src_after = src + '/' + id + '-after.jpg';            
    document.querySelector('.modal-baap-group-img-before').src = img_src_before;
    document.querySelector('.modal-baap-group-img-after').src = img_src_after;
  }
})