/*
 * MIT License
 *
 * Copyright (c) 2021 苗锦洲
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package tech.ordinaryroad.ioe.api.api;


import com.github.pagehelper.PageInfo;
import io.swagger.annotations.Api;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import tech.ordinaryroad.commons.core.base.result.Result;
import tech.ordinaryroad.ioe.api.constant.ServiceNameCons;
import tech.ordinaryroad.ioe.api.dto.IoEAlarmInfoDTO;
import tech.ordinaryroad.ioe.api.request.IoEAlarmInfoQueryRequest;
import tech.ordinaryroad.ioe.api.request.IoEEntityAlarmInfoQueryRequest;

import javax.validation.constraints.NotBlank;

/**
 * @author mjz
 * @date 2022/4/10
 */
@Api(value = "告警API")
@FeignClient(name = ServiceNameCons.SERVICE_NAME, contextId = "iIoEAlarmApi")
public interface IIoEAlarmApi {

    @DeleteMapping("/alarm/{id}/delete")
    Result<Void> delete(@PathVariable @Validated @NotBlank String id);

    @PostMapping("/alarm/{id}/ack")
    Result<Void> ack(@PathVariable @Validated @NotBlank String id);

    @PostMapping("/alarm/{id}/clear")
    Result<Void> clear(@PathVariable @Validated @NotBlank String id);

    @PostMapping("/alarm/list")
    Result<PageInfo<IoEAlarmInfoDTO>> list(@RequestBody @Validated IoEAlarmInfoQueryRequest request);

    @PostMapping("/alarm/list/entity")
    Result<PageInfo<IoEAlarmInfoDTO>> listEntity(@RequestBody @Validated IoEEntityAlarmInfoQueryRequest request);

}
