(function() {
	"use strict";

	// Easy selector helper function
	const select = (el, all = false) => {
		el = el.trim()
		if (all) {
			return [...document.querySelectorAll(el)]
		} else {
			return document.querySelector(el)
		}
	}

	// easy event listener func.
	const on = (type, el, listener, all = false) => {
		if (all) {
			select(el, all).forEach(e => e.addEventListener(type, listener))
		} else {
			select(el, all).addEventListener(type, listener)
		}
	}

	// easy on scroll event listener
	const onscroll = (el, listener) => {
		el.addEventListener('scroll', listener)
	}

	// sidebar toggle
	if (select('.toggle-sidebar-btn')) {
		on('click', '.toggle-sidebar-btn', function(e) {
			select('body').classList.toggle('toggle-sidebar')
		})
	}

	// search bar toggle
	if (select('.search-bar-toggle')) {
		on('click', '.search-bar-toggle', function(e) {
		select('.search-bar').classList.toggle('search-bar-show')
		})
	}

	// toggle class .header-scrolled to #header when page is scrolled
	let selectHeader = select('#header')
	if (selectHeader) {
		const headerScrolled = () => {
			if (window.scrollY > 100) {
				selectHeader.classList.add('header-scrolled')
			} else {
				selectHeader.classList.remove('header-scrolled')
			}
		}
		window.addEventListener('load', headerScrolled)
		onscroll(document, headerScrolled)
	}

	// back to top button
	let backtotop = select('.back-to-top')
	if (backtotop) {
		const toggleBacktotop = () => {
			if (window.scrollY > 100) {
				backtotop.classList.add('active')
			} else {
				backtotop.classList.remove('active')
			}
		}
		window.addEventListener('load', toggleBacktotop)
		onscroll(document, toggleBacktotop)
	}

	// init typing effect
	const typed = select('.typed')
	if (typed) {
		let typed_strings = typed.getAttribute('data-typed-items')
		typed_strings = typed_strings.split(',')
		new Typed('.typed', {
			strings: typed_strings,
			loop: true,
			typeSpeed: 100,
			backSpeed: 50,
			backDelay: 2000
		});
	}

	// init swiper slider with 3 slides at once in desktop view
	new Swiper('.slides-1', {
		speed: 600,
		loop: true,
		autoplay: {
			delay: 5000,
			disableOnInteraction: false
		},
		slidesPerView: 'auto',
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: true
		},
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		}
	});

	// auto-resize echarts
	const mainContainer = select('#main');
	if (mainContainer) {
		setTimeout(() => {
		new ResizeObserver(function() {
			select('.echart', true).forEach(getEchart => {
				echarts.getInstanceByDom(getEchart).resize();
			})
		}).observe(mainContainer);
		}, 200);
	}

	// Preloader
	let preloader = select('#preloader');
	if (preloader) {
		window.addEventListener('load', () => {
			preloader.remove()
		});
	}

})();