local Object = {}
Object.__index = Object

-- Constructor
function Object.new(param)
    local self = {}
    setmetatable(self, Object)

    self._privateProperty = "hidden"
    self.publicProperty = "visible"
    self._param = param

    return self
end

-- Method
function Object:getParam()
    return self._param
end

function Object:setParam(value)
    self._param = value
end

return Object
