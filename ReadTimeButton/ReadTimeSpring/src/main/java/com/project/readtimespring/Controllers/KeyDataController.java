package com.project.readtimespring.Controllers;

import com.project.readtimespring.Data.DataRepo;
import com.project.readtimespring.Data.GetData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.bind.annotation.*;

@RestController
@ComponentScan("com.project.readtimespring.Data.DataRepo")
public class KeyDataController {
    @Autowired
    DataRepo repo;

    @CrossOrigin
    @RequestMapping(value = "/ArrayData", method = RequestMethod.POST)
    public @ResponseBody
    GetData KeyData(@RequestBody GetData getData) {

        System.out.println(getData);
        repo.save(getData);
        return getData;


    }

    @GetMapping(path = "/all")
    public @ResponseBody
    Iterable<GetData> getAllUsers() {
        return repo.findAll();
    }


}
