const getOptionChart=async()=>{
    try{
        const response = await fetch("http://127.0.0.1:8000/api/get_chart/");
        return await response.json();
    }catch(ex){
        alert(ex);
    }
}

const initchart = async () => {
    const mychart = echarts.init(document.getElementById("chart"));

  
    mychart.setOption(await getOptionChart());
    mychart.resize();
}

window.addEventListener("load", async () => {
    await initchart();
})