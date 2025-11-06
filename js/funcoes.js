// Theme toggle: apply/remove `dark` class on <html> and persist preference in localStorage
(function () {
	function setTheme(dark) {
		const root = document.documentElement;
		const iconSun = document.getElementById('icon-sun');
		const iconMoon = document.getElementById('icon-moon');
		if (dark) {
			root.classList.add('dark');
			localStorage.setItem('theme', 'dark');
			if (iconSun) iconSun.classList.add('hidden');
			if (iconMoon) iconMoon.classList.remove('hidden');
		} else {
			root.classList.remove('dark');
			localStorage.setItem('theme', 'light');
			if (iconSun) iconSun.classList.remove('hidden');
			if (iconMoon) iconMoon.classList.add('hidden');
		}
	}

	document.addEventListener('DOMContentLoaded', function () {
		try {
			const saved = localStorage.getItem('theme');
			const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
			const initialDark = saved ? saved === 'dark' : prefersDark;
			setTheme(initialDark);

			const toggle = document.getElementById('theme-toggle');
			if (toggle) {
				toggle.addEventListener('click', function () {
					const isDark = document.documentElement.classList.contains('dark');
					setTheme(!isDark);
				});
			}
		} catch (e) {
			// swallow errors on very old browsers
			console.error('Theme toggle failed', e);
		}
	});
})();
