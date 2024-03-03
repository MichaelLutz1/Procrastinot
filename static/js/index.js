window.onload = () => {
	const resizeButton = document.getElementById('resize');
	const startButton = document.getElementById('start');
	const stopButton = document.getElementById('stop');
	startButton.addEventListener('click', async () => {
		const res = await fetch('/get_text?active=true')
		console.log(res)
	});
	stopButton.addEventListener('click', async () => {
		const res = await fetch('/get_text?active=false')
		console.log(res)
	});
	console.log(resizeButton)
	resizeButton.addEventListener('click', async () => {
		const res = await fetch('/resize')
		console.log(res)
	});
}
