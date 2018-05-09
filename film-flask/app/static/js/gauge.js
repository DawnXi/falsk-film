
	 var demo = echarts.init(document.getElementById('demo'));
	// 基于准备好的dom，初始化echarts实例
 option = {
    tooltip : {
        formatter: "{a} <br/>{c} {b}"
    },
    toolbox: {
        show: true,
        feature: {
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series :{
            name: '速度',
            type: 'gauge',
            z: 3,
            min: 0,
            max: 100,
            splitNumber: 10,
            radius: '150px',
            axisLine: {            // 坐标轴线
                lineStyle: {       // 属性lineStyle控制线条样式
                    width: 20
                }
            },
            axisTick: {            // 坐标轴小标记
                length: 5,        // 属性length控制线长
                lineStyle: {       // 属性lineStyle控制线条样式
                    color: '#fff'
                }
            },
            splitLine: {           // 分隔线
                length: 10,         // 属性length控制线长
                lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                    color: '#fff'
                }
            },
            axisLabel: {
            	fontSize:16,
                color: 'auto',
                distance:25
            },
            title : {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder',
                fontSize: 15,
                fontStyle: 'italic',
            },
            detail : {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                formatter: function (value) {
                    value = (value + '').split('.');
                    value.length < 2 && (value.push('00'));
                    return ('00' + value[0]).slice(-2)
                        + '.' + (value[1] + '00').slice(0, 2);
                },
                fontWeight: 'bolder',
                fontFamily: 'Arial',
                fontSize:15,
                color: 'blue',
                rich: {}
            },
            data:[{value: 40, name: '内存使用率'}]
        }
};

option2 = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    toolbox: {
        feature: {
            restore: {},
            saveAsImage: {}
        }
    },
    series: [
        {
            name: '业务指标',
            type: 'gauge',
            radius:'80%',
            detail: {
                formatter:'{value}%',
                fontSize: 16
            },
            title : {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder',
                fontSize: 15,
                fontStyle: 'italic',
            },
            data: [{value: 50, name: '内存使用率'}]
        }
    ]
};
