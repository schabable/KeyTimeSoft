package com.project.readtimespring.Data;


import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "keydata")
public class GetData {

    @Id
    long id;
    String name;
    int keyId;
    int timeClick;
    int timeNext;

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getKeyId() {
        return keyId;
    }

    public void setKeyId(int keyId) {
        this.keyId = keyId;
    }

    public int getTimeClick() {
        return timeClick;
    }

    public void setTimeClick(int timeClick) {
        this.timeClick = timeClick;
    }

    public int getTimeNext() {
        return timeNext;
    }

    public void setTimeNext(int timeNext) {
        this.timeNext = timeNext;
    }
}
