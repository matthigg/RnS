document.addEventListener('DOMContentLoaded', () => {
  
  const navbar = document.querySelector('.navbar');
  const nav_free_estimate = document.querySelector('.nav-free-estimate');

  // Change the appearance of the navbar when the user scrolls down the page
  window.addEventListener('scroll', () => {
    if (window.scrollY > 1) {

      // Shrink the navbar
      navbar.classList.add('navbar-minimized-true');
      navbar.classList.remove('navbar-minimized-false');

      // Reposition/move up the 'free estimate' button
      nav_free_estimate.classList.add('nav-free-quote-minimized');
      nav_free_estimate.classList.remove('nav-free-quote-maximized');
    } else {

      // Expand the navbar
      navbar.classList.add('navbar-minimized-false');
      navbar.classList.remove('navbar-minimized-true');

      // Reposition/move down the 'free estimate' button
      nav_free_estimate.classList.add('nav-free-quote-maximized');
      nav_free_estimate.classList.remove('nav-free-quote-minimized');
    }
  })

  // Underline Active Navbar Links & Toggle Free Estimate Button Visibility
  //
  // Assign the .active class to the current page's nav-link which decorates it
  // with an underscore (to give an indication which page is the current page)
  // & show the 'Free Estimate' button in index, services, our work, and about
  // pages.
  if (document.querySelector('.container-fluid').classList.contains('index-page')) {
    document.querySelector('.nav-link-home').classList.add('active');
    document.querySelector('.nav-free-estimate').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('services-page')) {
    document.querySelector('.nav-link-services').classList.add('active');
    document.querySelector('.nav-free-estimate').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('our-work-page')) {
    document.querySelector('.nav-link-our-work').classList.add('active');
    document.querySelector('.nav-free-estimate').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('about-page')) {
    document.querySelector('.nav-link-about').classList.add('active');
    document.querySelector('.nav-free-estimate').style.display = 'block';
  } else if (document.querySelector('.container-fluid').classList.contains('contact-page')) {
    document.querySelector('.nav-link-contact').classList.add('active');
  }

  // Contact Form Required Fields
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
// Add a 'click' event listener to each 'before-and-after' group of images that
// looks for a data-category attribute and, if it finds one, grabs the before &
// after image URL's, hosted on AWS S3, and sends them to the modal template for
// display.
  const baap_groups = document.querySelectorAll('.our-work-baap-group');
  baap_groups.forEach((baap_group) => {
    baap_group.addEventListener('click', (event) => {
      let element = event.target;
      if (element.dataset.category === undefined) {
        while (element.parentNode) {
          element = element.parentNode;
          if (element.dataset.category) {
            assignModalBAAPImage(element.dataset.beforeSrc, element.dataset.afterSrc);
            return
          } 
        }
      } else {
        assignModalBAAPImage(element.dataset.beforeSrc, element.dataset.afterSrc);
      }
    })
  })
  function assignModalBAAPImage(before_src, after_src) {
    document.querySelector('.modal-baap-group-img-before').src = before_src
    document.querySelector('.modal-baap-group-img-after').src = after_src
  }

  // Modals, single images
  const single_images = document.querySelectorAll('.our-work-single-image-wrapper');
  single_images.forEach((single_image) => {
    single_image.addEventListener('click', (event) => {
      let element = event.target;
      if (element.dataset.category === undefined) {
        while (element.parentNode) {
          element = element.parentNode;
          if (element.dataset.category) {
            console.log(element.dataset.category)
            assignModalSingleImage(element.dataset.singleSrc);
            return
          } 
        }
      } else {
        console.log(element.dataset.category)
        assignModalSingleImage(element.dataset.singleSrc);
      }
    })
  })
  function assignModalSingleImage(single_src) {
    console.log(single_src)
    document.querySelector('.modal-single-image-element').src = single_src;
  }

  // User clicked 'Call Now' button -- call phone number
  document.querySelector('.nav-call-now').addEventListener('click', () => {
    gtag('event', 'click_call_now_button', {
      'event_category': 'engagement',
      'event_label': 'User clicked the call button to make a phone call',
      'value': '50',
      'event_callback': function() {
        window.open('tel:+1-804-258-0403', '_self')
      },
    });
  })

  // User clicked 'FREE Estimate' button -- go to contact page
  document.querySelector('.nav-free-estimate').addEventListener('click', (event) => {
    gtag('event', 'click_free_quote_button', {
      'event_category': 'engagement',
      'event_label': 'User clicked the free quote button to go to the Contact Us page',
      'value': '0',
      'event_callback': function() {
        window.open(window.location.origin + event.target.dataset.url, '_self')
      },
    });
  })
})