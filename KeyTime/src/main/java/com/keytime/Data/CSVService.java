package com.keytime.Data;

import java.util.List;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

@Service
@Transactional
public class CSVService {
    @Autowired
    private DataRepo repo;

    public List<GetData> listAll() {
        return repo.findAll(Sort.by("name").and(Sort.by("id")).ascending());
    }
}