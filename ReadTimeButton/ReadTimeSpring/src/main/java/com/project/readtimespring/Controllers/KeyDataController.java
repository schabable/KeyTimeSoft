package com.project.readtimespring.Controllers;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.project.readtimespring.Data.CSVService;
import com.project.readtimespring.Data.DataRepo;
import com.project.readtimespring.Data.GetData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.*;
import org.supercsv.io.CsvBeanWriter;
import org.supercsv.io.ICsvBeanWriter;
import org.supercsv.prefs.CsvPreference;


import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.util.List;

@RestController
@ComponentScan("com.project.readtimespring.Data.DataRepo")
public class KeyDataController {
    @Autowired
    DataRepo repo;


    @CrossOrigin
    @RequestMapping(value = "/ArrayData", method = RequestMethod.POST)
    public @ResponseBody
    GetData KeyData(@RequestBody GetData getData) throws IOException {


        System.out.println(getData);
        repo.save(getData);
        return getData;
    }

    @Autowired
    ObjectMapper objectMapper;

    @Autowired
    ResourceLoader resourceLoader;

    @GetMapping("/json")
    public File test() throws IOException {
        File file = new ClassPathResource("./report.json").getFile();
        return file;

    }


    @GetMapping(path = "/all")
    public @ResponseBody
    List<GetData> getAllUsers() {
        return repo.findAll(Sort.by("id").and(Sort.by("name").ascending()));
    }


    @Autowired
    private CSVService service;


    @GetMapping(path = "/export")
    public void exportToCSV(HttpServletResponse response) throws IOException {
        response.setContentType("text/csv");

        String headerKey = "Content-Disposition";
        String headerValue = "attachment; filename=data.csv;";
        response.setHeader(headerKey, headerValue);


        List<GetData> listData = service.listAll();

        ICsvBeanWriter csvWriter = new CsvBeanWriter(response.getWriter(), CsvPreference.STANDARD_PREFERENCE);
        String[] csvHeader = {"ID", "name", "KeyCode", "TimeClick", "TimeNext"};
        String[] nameMapping = {"id", "name", "keyCode", "timeClick", "timeNext"};


        csvWriter.writeHeader(csvHeader);

        for (GetData data : listData) {
            csvWriter.write(data, nameMapping);
        }

        csvWriter.close();

    }


}
