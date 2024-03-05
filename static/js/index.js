window.onload = () => {
	const resizeButton = document.getElementById('resize');
	const startButton = document.getElementById('start');
	const stopButton = document.getElementById('stop');
	const graphButton = document.getElementById('graph');
	startButton.addEventListener('click', async () => {
		const res = await fetch('/get_text?active=true')
		console.log(res)
	});
	stopButton.addEventListener('click', async () => {
		const res = await fetch('/get_text?active=false')
		console.log(res)
	});
	resizeButton.addEventListener('click', async () => {
		const res = await fetch('/resize')
		console.log(res)
	});
	graphButton.addEventListener('click', async () => {
		// const res = await fetch('/graph_data')
		// const data = await res.json()
		// console.log(data)
		location.reload()
	});
}
