    var map = new AMap.Map("container", {});
    var truckOptions = {
            map: map,
            policy:0,
            size:1,
            city:'beijing',
            panel:'panel'
    };
    map.plugin('AMap.TruckDriving',function () {
        var driving = new AMap.TruckDriving(truckOptions);
        var path = [
            {keyword:'马鞍山市',city:'010'},//起点
            {keyword:'{{ destination }}',city:'010'}//终点
        ];
        driving.search(path, function(status, result) {
        if (status === 'complete') {
            log.success('绘制路线完成')
        } else {
            log.error('获取规划数据失败：' + result)
        }
        });
    });